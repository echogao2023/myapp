import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;
import java.util.Collections;
import java.util.Map;

import okhttp3.*;

@SpringBootApplication
@RestController
public class WeChatBotApplication {

    // 填入你的图灵机器人API key
    private static final String TURING_API_KEY = "1c99470a8a8354e248a4c229234d14af";

    public static void main(String[] args) {
        SpringApplication.run(WeChatBotApplication.class, args);
    }

    @PostMapping(path = "/wechat")
    public Map<String, Object> handleWeChatMessage(@RequestBody Map<String, Object> requestBodyMap) {
        String message = getMessageFromRequest(requestBodyMap);

        if (message != null) {
            String reply = getTuringReply(message);

            if (reply != null) {
                String responseXml = createXMLResponse(requestBodyMap, reply);
                return successResponse(responseXml);
            }
        }

        return successResponse();
    }

    /**
     * 解析微信服务器POST请求过来的消息体，提取出用户发送的文本消息。
     */
    private String getMessageFromRequest(Map<String, Object> requestBodyMap) {
        try {
            // 获取消息类型
            String msgType = (String) requestBodyMap.get("MsgType");

            if ("text".equals(msgType)) {
                // 接收到文本消息，解析出消息内容
                return (String) requestBodyMap.get("Content");
            } else {
                // 接收到其他消息类型，忽略并返回null
                return null;
            }
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }

    /**
     * 调用图灵机器人API获取回复消息。
     */
    private String getTuringReply(String message) {
        OkHttpClient = new OkHttpClient（）;
        String apiUrl = "http://openapi.tuling123.com/openapi/api/v2";

        MediaType mediaType = MediaType.parse("application/json; charset=utf-8");
        RequestBody body = RequestBody.create(mediaType, createTuringRequestBodyJson(message));

        Request request = new Request.Builder()
        .url(apiUrl)
        .post(body)
        .build();

        try (Response response = client.newCall(request).execute()) {
            if (!response.isSuccessful()) {
                throw new IOException("Unexpected response code: " + response);
            }

            String responseBody = response.body().string();
            return parseTuringReplyJson(responseBody);
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }

    /**
     * 构造图灵机器人请求的JSON字符串。
     */
    private String createTuringRequestBodyJson(String message) {
        ObjectMapper objectMapper = new ObjectMapper();
        TuringRequestBody requestBody = new TuringRequestBody();
        TuringRequestBody.InputText inputText = new TuringRequestBody.InputText();
        inputText.setText(message);
        requestBody.setInputText(inputText);
        requestBody.setApiKey(TURING_API_KEY);
        requestBody.setUserId("123456");
        TuringRequestBody.Perception perception = new TuringRequestBody.Perception();
        perception.setInputText(inputText);
        requestBody.setPerception(perception);

        try {
            return objectMapper.writeValueAsString(requestBody);
        } catch (JsonProcessingException e) {
            e.printStackTrace();
            return null;
        }
    }

    /**
     * 解析图灵机器人的响应结果，提取出回复消息。
     */
    private String parseTuringReplyJson(String responseBody) throws IOException {
        ObjectMapper objectMapper = new ObjectMapper();
        TuringResponseBody turingResponse = objectMapper.readValue(responseBody, TuringResponseBody.class);
        TuringResponseBody.Results[] resultsArray = turingResponse.getResults();

        if (resultsArray != null && resultsArray.length > 0 && resultsArray[0].getValues() != null) {
            return resultsArray[0].getValues().getText();
        } else {
            throw new IOException("Failed to parse reply from Turing API response: " + responseBody);
        }
    }

    /**
     * 根据微信消息格式创建回复消息的XML字符串。
     */
    private String createXMLResponse(Map<String, Object> requestBodyMap, String reply) {
        String fromUserName = (String) requestBodyMap.get("FromUserName");
        String toUserName = (String) requestBodyMap.get("ToUserName");

        StringBuilder xmlBuilder = new StringBuilder