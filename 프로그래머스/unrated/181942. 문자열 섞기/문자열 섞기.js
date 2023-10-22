function solution(str1, str2) {
    var answer = '';
    var mLen = Math.max(str1.length, str2.length);

    for (var i = 0; i < mLen; i++) {
        if (i < str1.length) {
            answer += str1[i];
        }   
        if (i < str2.length) {
            answer += str2[i];
        }
    }

    return answer;
}