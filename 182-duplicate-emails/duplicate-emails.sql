# Write your MySQL query statement below 
SELECT DISTINCT P1.EMAIL FROM PERSON P1 JOIN PERSON P2 ON P1.EMAIL=P2.EMAIL AND P1.ID!=P2.ID 