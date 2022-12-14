# <strong>Backend

[![Maintainability](https://api.codeclimate.com/v1/badges/203b7f73823c7e2b1567/maintainability)](https://codeclimate.com/github/DongGuk-Seo/Backend/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/203b7f73823c7e2b1567/test_coverage)](https://codeclimate.com/github/DongGuk-Seo/Backend/test_coverage)
<br>
<br>

## ๐ฅ <strong>Skills
---
<br>

[![My Skills](https://skillicons.dev/icons?i=python,django,mysql,nginx,git,github,githubactions,aws,aws_s3)](https://skillicons.dev)

<br>

Ohters : <br>
- Django-Rest-Framework (DRF)
- Simplejwt (DRF)
- Gunicorn (Middleware)
- AWS EC2
- AWS S3
- AWS RDS
- Pytest
- Code Climate

## <a href="https://github.com/melonmarket#architecture"> Show all the architecture (click) </a>
<br>
<br>


## ๐ <strong>ERD</strong>
---
<br>
 <img width="604" alt="แแณแแณแแตแซแแฃแบ 2022-12-18 แแฉแแฅแซ 12 58 00" src="https://user-images.githubusercontent.com/94242504/208285846-fbddcda5-44e5-4141-9775-08f1b2c1a9ca.png">

<br>
<br>


## ๐ฟ <strong>Role</strong>
---
 - **๊ธฐ๋ณธ Api ๊ธฐ๋ฅ ๊ตฌํ**
    - ํ์๊ฐ์ ๋ฐ ๋ก๊ทธ์ธ : DRF์ Simplejwt๋ฅผ ์ด์ฉํ ํ์ ๊ด๋ฆฌ
    - ์ด๋ฉ์ผ ์ค๋ณต ์ฒดํฌ : ์ด๋ฉ์ผ ์ฌ์  ์ค๋ณต ํ์ธ ๊ธฐ๋ฅ
    - ๊ฒ์๊ธ CRUD : ๊ฒ์๊ธ ์์ฑ, ํ์ธ, ์์ , ์ญ์  ๊ธฐ๋ฅ
    - ๋ฉ์ธ ํ์ด์ง ํ์ธ : ์์ฒญ ์ ์ต๊ทผ ๊ฒ์๊ธ 5๊ฐ์ฉ Pagination ์ ์ฉํ์ฌ ์๋ต
    - ์์ธ ํ์ด์ง ํ์ธ: ์์ธ ํ์ด์ง ๋ด์ฉ๊ณผ ํจ๊ป ๊ธ์ด์ด์ ์ต๊ทผ 4๊ฐ ๊น์ง์ ๊ฒ์๋ฌผ์ ํจ๊ป ์๋ต
    - ์ข์์ ๊ธฐ๋ฅ : ์ฌ์ฉ์๊ฐ ์์ธ ํ์ด์ง ๋ด์์ ์ข์์ ๋ฐ ํด์ ๊ฐ ๊ฐ๋ฅํ ๊ธฐ๋ฅ (๋ฉ์ธ ํ์ด์ง์์ ์ข์์ ์ ํ์ธ ๊ฐ๋ฅ)
    - ์กฐํ์ ๊ธฐ๋ฅ : ์์ธ ํ์ด์ง๋ฅผ ์ฝ์ ์กฐํ์๋ฅผ ๋ฉ์ธํ์ด์ง ๋๋ ์์ธํ์ด์ง์์ ํ์ธ (์ฟ ํค๋ฅผ ์ด์ฉํ์ฌ 5์๊ฐ ๋ด ์ค๋ณต ์กฐํ ์ ์ธ)
    - ์นดํ๊ณ ๋ฆฌ ๊ธฐ๋ฅ : ์นดํ๊ณ ๋ฆฌ๋ณ ์ต๊ทผ ๊ฒ์๋ฌผ ํ์ธ ๊ธฐ๋ฅ
    - ๊ฒ์ ๊ธฐ๋ฅ : ์ ๋ชฉ ๊ธฐ์ค์ ๊ฒ์ ๊ธฐ๋ฅ

<br>

 - **AWS Setup**
    - AWS S3 : ์ ์  ํ๋กํ ์ฌ์ง๊ณผ ๊ฒ์๊ธ ์ฌ์ง์ AWS S3์ ์ฐ๊ฒฐํ์ฌ ์๋ก๋
    - AWS RDS : Mysql Database setup ํ Django(WAS)์ ์ฐ๊ฒฐํ์ฌ ์ฌ์ฉ
    - AWS EC2 : Django, gunicorn ๋ฐ nginx setup ํ ๋ฐฐํฌ

<br>

 - **CI/CD**
    - Pytest, Coverage : Unit ๋จ์์ Test Code ์์ฑ ํ Coverage ํ์ธ
    - Github Actions (CI) : develop branch์ Pull-Request์ Test Code ๋ฐ Coverage ํ์คํธ
    - Github Actions (CD) : ํ์คํธ๋ฅผ ๋ง์น ์ฝ๋๋ค์ S3์ ์ ์ฅ ํ Code Deploy๋ฅผ ํตํด EC2์ ์๋ฒ ๋ฐฐํฌ

<br>
<br>

## ๐  <strong>Trouble Shoot</strong>

<br>

### <strong> 1. ๋ก๊ทธ์ธ ์ Authenticated๊ฐ ํ์์๋๋ก ์ค์ ํ์์ผ๋ Headers์ Authorization ๋ถ๋ถ์ด ์กด์ฌํ๋ฉด ํญ์ 403 Forbidden ์๋ฌ๊ฐ ๋ฐ์ </strong>

<br>
ํด๊ฒฐ : Default Class๋ก IsAuthenticated๋ฅผ ํด์งํ์ฌ๋ ๊ฐ์ ์๋ฌ๊ฐ ๋ฐ์ํ์๊ณ  ํด๋น ์๋ฌ๋ Sign-in View์์ Authentication_classes๋ฅผ ๋น ๋ฆฌ์คํธ๋ก overrideํ์ฌ ํด๊ฒฐ
<br>

<img width="380" alt="แแณแแณแแตแซแแฃแบ 2022-12-14 แแฉแแฅแซ 2 16 22" src="https://user-images.githubusercontent.com/94242504/207400052-3af43bfe-b428-4205-8e7d-cb47e48b9817.png">


<br>
<br>

### <strong> 2. ๊ฒ์๊ธ ์์ฑ/์์  ์ Serializer์ SerializedMethod๋ฅผ ์ด์ฉํ์ฌ ํ์ผ์ ๊ฐ๋ณ ๋ถ๋ฆฌ ํ ์ ์ฅํ์์ผ๋ ์ด๋ฏธ์ง ํ์ผ์ด ์๊ฑฐ๋ ์๋ชป๋ ํ์์ด๋ผ๋ Null ๊ฐ์ผ๋ก ์ ์ฅ๋๋ ์๋ฌ๊ฐ ๋ฐ์</strong>

<br>
<div align='center'>
<img width="634" alt="แแณแแณแแตแซแแฃแบ 2022-12-15 แแฉแแฎ 2 25 42" src="https://user-images.githubusercontent.com/94242504/207779670-4b9cac0d-0b5b-48f6-ad01-94cd0afe9827.png">
</div>
<br>
ํด๊ฒฐ : ImageSerializer ๋จ๊ณ์์ ์ด๋ฏธ์งํ์ผ์ ์ฐ์ ์ ์ผ๋ก ๋ฐ์ ๋ค์ ์ด๋ฏธ์ง๊ฐ ์์ผ๋ฉด ValidationError์ ๋ฐ์ํ๋๋ก ์์ 

<div align='center'>
<img width="671" alt="แแณแแณแแตแซแแฃแบ 2022-12-15 แแฉแแฎ 2 33 33" src="https://user-images.githubusercontent.com/94242504/207780607-2425c07d-4122-4c61-aefe-bb92309bbd8b.png">
</div>

<br>
<br>

### <strong>3. Pytest๋ก Test Code ์์ฑํ  ๋ dummy ๊ฒ์๊ธ ์์ฑ ์ค Image์์ Content-Type ์๋ฌ ๋๋ Encoding ์๋ฌ ๋ฐ์</strong>

<br>
ํด๊ฒฐ : <br> 
1. ์ ์กํ  ์ด๋ฏธ์ง๋ฅผ ๋ถ๋ฌ์ฌ ๋ django์ SimpleUploadedFile์ ์ด์ฉํ์ฌ ์ด๋ฏธ์ง๋ฅผ ์ฝ์ด์์ Encoder๋ก ์ด๋ฏธ์ง ์ ๋ฌ
<br>
2. Multipart/form-data ํ์์ผ๋ก Encodingํ๊ธฐ ์ํ์ฌ requests_toolbelt์ MultipartEncoder๋ฅผ ์ด์ฉํ์ฌ Encoding ํ ๋ฐ์ดํฐ๋ฅผ post Method๋ก ์ ๋ฌ
<br>

<div align='center'>
<img width="433" alt="แแณแแณแแตแซแแฃแบ 2022-12-15 แแฉแแฎ 5 24 11" src="https://user-images.githubusercontent.com/94242504/207809370-32232da5-2db8-43dd-919d-0f8c577dfbaf.png">
</div>

