class Solution {
    public String solution(String cipher, int code) {
        StringBuilder answer = new StringBuilder();
        int end = cipher.length() / code;

        for(int i = 1; i <= end; i++) {
            answer.append(cipher.charAt(code * i - 1));
        }

        return answer.toString();
    }
}