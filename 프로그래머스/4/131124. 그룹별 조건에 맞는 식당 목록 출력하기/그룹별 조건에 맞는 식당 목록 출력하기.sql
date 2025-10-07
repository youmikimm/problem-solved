SELECT A.MEMBER_NAME
     , B.REVIEW_TEXT
     , TO_CHAR(B.REVIEW_DATE, 'YYYY-MM-DD') AS REVIEW_DATE
  FROM MEMBER_PROFILE A
     , REST_REVIEW B
 WHERE A.MEMBER_ID = B.MEMBER_ID
   AND A.MEMBER_ID IN (SELECT MEMBER_ID
                         FROM REST_REVIEW
                        GROUP BY MEMBER_ID
                       HAVING COUNT(1) = (SELECT MAX(COUNT(1))
                                            FROM REST_REVIEW
                                           GROUP BY MEMBER_ID))
 ORDER BY B.REVIEW_DATE, B.REVIEW_TEXT