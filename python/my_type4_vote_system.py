member = ["황준석", "한지우", "안승환", "박지원", "박시현", "박민석"]

pick = [
    "4. 덩그러니-나상현싸뱐드, 7. Ocean colour scene - Hundred mile high city, 8. panic station - muse, 10. 사랑으로 wave to earth, 11. 낭만 젊음 사랑 이세계, 21. 21세기의 어떤 날 - 페퍼톤스, 25. sakanaction / Shin Takarajima, 26. sakanaction - 잊을 수가 없어, 27. happier than ever 빌리아일리시, 28. 너드커넥션 그대만 있다몈, 35. unholy cover by yudabinband, 36. Muse - Starlight, 37. 조지 - 보트",
    "1. 괴수의 꽃노래(怪獣の花唄) - Vaundy, 2. Pretender - 오피셜히게단디즘, 3. with you(band ver) - 하현상, 4. 덩그러니-나상현싸뱐드, 5. Don’t be afraid-더폴스, 6. Calla-wave to earth, 8. panic station - muse, 9. pueblo wave to earth, 11. 낭만 젊음 사랑 이세계, 13. i love you 라쿠나, 19. 독하게 - 한요한, 20. Lost my phone - 조매력, 21. 21세기의 어떤 날 - 페퍼톤스, 22. give me a kiss - crash adams, 23. TOOOOOO - 라쿠나, 24. Seven - 정국, 26. sakanaction - 잊을 수가 없어, 30. 웨투어 daisy, 31. Honne - Warm on a christmas night, 33. 디지몬 어드벤쳐 극장판 오프닝 - Butterfly, 34. Just the two of us cover by HSCC, 35. unholy cover by yudabinband, 36. Muse - Starlight, 37. 조지 - 보트",
    "3. with you(band ver) - 하현상, 4. 덩그러니-나상현싸뱐드, 5. Don’t be afraid-더폴스, 6. Calla-wave to earth, 12. rest 백예린, 14. robbers the 1975, 17. say it ain so weezer, 22. give me a kiss - crash adams, 27. happier than ever 빌리아일리시, 29. 짙은 해바라기, 31. Honne - Warm on a christmas night, 34. Just the two of us cover by HSCC, 36. Muse - Starlight, 37. 조지 - 보트",
    "13. i love you 라쿠나",
    "2. Pretender - 오피셜히게단디즘, 3. with you(band ver) - 하현상, 4. 덩그러니-나상현싸뱐드, 5. Don’t be afraid-더폴스, 6. Calla-wave to earth, 9. pueblo wave to earth, 10. 사랑으로 wave to earth, 11. 낭만 젊음 사랑 이세계, 13. i love you 라쿠나, 14. robbers the 1975, 15. simple imagination young gun silver fox, 16. 난 아직도 콜드, 17. say it ain so weezer, 20. Lost my phone - 조매력, 21. 21세기의 어떤 날 - 페퍼톤스, 22. give me a kiss - crash adams, 27. happier than ever 빌리아일리시, 28. 너드커넥션 그대만 있다몈, 29. 짙은 해바라기, 30. 웨투어 daisy, 31. Honne - Warm on a christmas night, 34. Just the two of us cover by HSCC, 37. 조지 - 보트",
    "2. Pretender - 오피셜히게단디즘, 8. panic station - muse, 12. rest 백예린, 21. 21세기의 어떤 날 - 페퍼톤스, 22. give me a kiss - crash adams, 24. Seven - 정국, 26. sakanaction - 잊을 수가 없어, 33. 디지몬 어드벤쳐 극장판 오프닝 - Butterfly, 34. Just the two of us cover by HSCC, 35. unholy cover by yudabinband, 36. Muse - Starlight, 37. 조지 - 보트",
]

pick_1 = [
    "28. 너드커넥션 그대만 있다몈",
    "21. 21세기의 어떤 날 - 페퍼톤스",
    "6. Calla-wave to earth",
    "13. i love you 라쿠나",
    "27. happier than ever 빌리아일리시",
    "33. 디지몬 어드벤쳐 극장판 오프닝 - Butterfly",
]

pick_2 = [
    "11. 낭만 젊음 사랑 이세계",
    "34. Just the two of us cover by HSCC",
    "31. Honne - Warm on a christmas night",
    "13. i love you 라쿠나",
    "9. pueblo wave to earth",
    "2. Pretender - 오피셜히게단디즘",
]

score = [[0] * 7 for _ in range(38)]
for i, p in enumerate(pick):
    s_p = p.split(", ")
    for song in s_p:
        s_song = song.split(". ")
        score[int(s_song[0])][i] += 1

for i, p in enumerate(pick_1):
    s_p = p.split(". ")
    score[int(s_p[0])][i] += 5

for i, p in enumerate(pick_2):
    s_p = p.split(". ")
    score[int(s_p[0])][i] += 4

for i in range(38):
    score[i][6] = sum(score[i])


print(*score)
