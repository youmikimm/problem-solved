-- 코드를 입력하세요
SELECT A.ANIMAL_ID, A.ANIMAL_TYPE, A.NAME
  FROM ANIMAL_INS A
 WHERE A.SEX_UPON_INTAKE LIKE 'Intact%'
   AND A.ANIMAL_ID IN (SELECT ANIMAL_ID
                         FROM ANIMAL_OUTS
                        WHERE SEX_UPON_OUTCOME LIKE 'Spayed%' 
                           OR SEX_UPON_OUTCOME LIKE 'Neutered%'
                      )
ORDER BY A.ANIMAL_ID
;