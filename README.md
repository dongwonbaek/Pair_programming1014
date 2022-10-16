### 김예린 님, 조창현 님과 함께 개발한 영화리뷰 커뮤니티 서비스입니다.



## 목표
- **CRUD** 구현
- Django **Auth** 활용 회원 관리(회원가입 / 회원 조회 / 로그인 / 로그아웃)
- git 을 통한 협업과정 숙달

---
#### Git 활용 과정

❗ 각 과정 완료 후 

[로컬/드라이버] accounts/detail → [원격/드라이버] accounts/detail,  Commit & Push 수행

[원격/드라이버] accounts/detail → [원격/드라이버] main, PR 생성 & Merge 수행

[원격/드라이버] accounts/detail 브랜치 삭제

[원격/전체] main → [로컬/전체] main, Pull 수행

드라이버 변경

[로컬/새 드라이버] accounts/update 브랜치에서 다음 토픽 진행

---


### 앱 이름 : accounts

### 1. 회원가입

`branch accounts/signup`

모델 이름 : User

- Django **AbstractUser** 모델 상속

**폼 Form**

- Django 내장 회원가입 폼 UserCreationForm을 상속 받아서 CustomUserCreationForm 작성, 해당 폼은 아래 필드만 출력
  
    - username
    - password1
    - password2, 

**기능 View**

회원가입

- `POST` http://127.0.0.1:8000/accounts/signup/
- CustomUserCreationForm을 활용해서 회원가입 구현

**화면 Template**

회원가입 페이지

- `GET` http://127.0.0.1:8000/accounts/signup/
- 회원가입 폼

---

### 2. 로그인

`branch accounts/login`

**폼 Form**

로그인

- Django 내장 로그인 폼 **AuthenticationForm 활용**

**기능 View**

로그인

- `POST` http://127.0.0.1:8000/accounts/login/
- **AuthenticationForm**를 활용해서 로그인 구현

**화면 Template**

로그인 페이지

- `GET` http://127.0.0.1:8000/accounts/login/
- 로그인 폼
- 회원가입 페이지 이동 버튼

---

### 3. 회원 목록 조회

`branch accounts/index`

**기능 View**

회원 목록 조회

- `GET` http://127.0.0.1:8000/accounts/

**화면 Template**

회원 목록 페이지

- `GET` http://127.0.0.1:8000/accounts/
- 회원 목록 출력
- 회원 아이디를 클릭하면 해당 회원 조회 페이지로 이동

---

### 4. 회원 정보 조회

`branch accounts/detail`

**기능 View**

회원 정보 조회

- `GET` http://127.0.0.1:8000/accounts/\<int:user_pk>/

**화면 Template**

회원 조회 페이지(프로필 페이지)

- `GET` http://127.0.0.1:8000/accounts/\<int:user_pk>/


---

### 5. 회원 정보 수정

`branch accounts/update`

**폼 Form**

회원 정보 수정

- Django 내장 회원 수정 폼 UserChangeForm을 상속 받아서 **CustomUserChangeForm** 작성
  
    해당 폼은 아래 필드만 출력.
    
    - first_name
    - last_name
    - email

**기능 View**

회원 정보 수정

- `POST` http://127.0.0.1:8000/accounts/update/

회원 비밀번호 수정 

- update_session_auth_hash 를 활용하여 비밀번호가 변경되어도 세션을 유지할 수 있도록 함.

- POST http://127.0.0.1:8000/accounts/password/

**화면 Template**

회원 정보 수정 페이지

- `GET` http://127.0.0.1:8000/accounts/update/

---

### 6. 로그아웃

`branch accounts/logout`

**기능 View**

로그아웃

- `POST` http://127.0.0.1:8000/accounts/logout/

---

### 7. 네비게이션바

`branch template/navbar`

**화면 Template**

**네비게이션바**

- 리뷰 목록 페이지 이동 버튼

- 리뷰 작성 페이지 이동 버튼

- 비 로그인 유저는 작성 버튼 출력 X

    ~~~html
    {% if request.user.is_authenticated %}
    	<a href="{% url 'accounts:create' %}">작성</a>
    {% endfor %}
    ~~~

- 로그인 상태에 따라 다른 화면 출력
    1. 로그인 상태
        - 로그인 한 사용자의 username 출력
            - username을 클릭하면 마이 페이지로 이동
        - 로그아웃 버튼
    2. 비 로그인 상태 
        - 로그인 페이지 이동 버튼 `(django auth의 decorators 기능 중 login_required 기능을 활용)`
        - 회원가입 페이지 이동 버튼

---

### 8. 리뷰 생성

`branch reviews/create`

**앱 App**

앱 이름 : reviews

모델 Model

모델 이름 : Review

- 모델 필드
  
  
    | 이름 | 역할 | 필드 | 속성 |
    | --- | --- | --- | --- |
    | title | 리뷰 제목 | Char | max_length=80 |
    | content | 리뷰 내용 | Text |  |
    | movie_name | 영화 이름 | Char | max_length=80 |
    | grade | 영화 평점 | Integer | validators=[MinValueValidator(0), MaxValueValidator(10)] |
    | created_at | 리뷰 생성시간 | DateTime | auto_now_add=True |
    | updated_at | 리뷰 수정시간 | DateTime | auto_now = True |
    | user_name | 작성자 | ForeignKey | User, on_delete=models.CASCADE, null=True |

**기능 View**

데이터 생성

- `POST` http://127.0.0.1:8000/reviews/create/

**화면 Template**

**리뷰 작성 페이지**

- `GET` http://127.0.0.1:8000/reviews/create/
- 리뷰 작성 폼(ReviewForm)

---

### 9. 리뷰 목록 조회

`branch reviews/index`

**기능 View**

데이터 목록 조회

- `POST` http://127.0.0.1:8000/reviews/

**화면 Template**

리뷰 **목록 페이지** 

- `GET` http://127.0.0.1:8000/reviews/
- 리뷰 목록 출력
- 제목을 클릭하면 해당 리뷰의 정보 페이지로 이동

---

### 10. 리뷰 정보 조회

`branch reviews/detail`

**기능 View**

데이터 정보 조회

- `GET` http://127.0.0.1:8000/reviews/<int:review_pk>/

**화면 Template**

**리뷰 정보 페이지**

- `GET` http://127.0.0.1:8000/reviews/<int:review_pk>/
- 해당 리뷰 정보 출력
- 수정 / 삭제 버튼

---

### 11. 리뷰 정보 수정

`branch reviews/update`

**기능 View**

데이터 수정

- `POST` http://127.0.0.1:8000/reviews/<int:review_pk>/update/

**화면 Template**

**리뷰 수정 페이지**

- `GET` http://127.0.0.1:8000/reviews/<int:review_pk>/update/
- 리뷰 수정 폼

---

### 12. 리뷰 삭제

`branch reviews/delete`

**기능 View**

데이터 삭제

- `POST` http://127.0.0.1:8000/reviews/<int:review_pk>/delete
