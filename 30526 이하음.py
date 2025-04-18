class Book:
    def __init__(self, title, author, description):
        self.title = title
        self.author = author
        self.description = description
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []
        self.font_scale = 1  # 1: 기본, 2: 크게, 3: 더 크게

    def set_font_scale(self, scale):
        if 1 <= scale <= 3:
            self.font_scale = scale

    def format_text(self, text):
        if self.font_scale == 1:
            return text
        elif self.font_scale == 2:
            return f"*{text}*"
        elif self.font_scale == 3:
            return f"**{text.upper()}**"

    def add(self, title, author, description):
        self.books.append(Book(title, author, description))

    def remove(self, index):
        if 0 <= index < len(self.books):
            del self.books[index]

    def borrow(self, index):
        if 0 <= index < len(self.books) and not self.books[index].is_borrowed:
            self.books[index].is_borrowed = True

    def return_(self, index):
        if 0 <= index < len(self.books) and self.books[index].is_borrowed:
            self.books[index].is_borrowed = False

    def edit(self, index, title, author, description):
        if 0 <= index < len(self.books):
            self.books[index].title = title
            self.books[index].author = author
            self.books[index].description = description

    def show(self):
        for i, book in enumerate(self.books):
            status = "대출 가능" if not book.is_borrowed else "대출 중"
            title = self.format_text(book.title)
            author = self.format_text(book.author)
            print(f"{i}. {title} - {author} [{status}]")

    def show_description(self, index):
        if 0 <= index < len(self.books):
            book = self.books[index]
            print(f"\n📖 '{book.title}'의 설명:\n{book.description}\n")
            self.speak(f"{book.title}. {book.description}")
        else:
            print("잘못된 도서 번호입니다.")

# 도서 목록 초기화
library = Library()
library.add("혼자 공부하는 파이썬", "윤인성", "파이썬 입문자를 위한 기초서로, 예제 중심 학습 제공")
library.add("산업경영공학개론", "고시근", "산업공학의 기초 개념과 경영 적용 사례를 다룸")
library.add("스마트 세상을 여는 산업공학","대한산업공학회", "산업공학의 최신 트렌드와 응용 분야 소개")
library.add("산업경영공학","박용태", "이론 중심의 산업공학 개론서")
library.add("스마트 스웜","Miller", "군집 지능을 통한 문제 해결의 미래를 탐구함")

# 메뉴 루프
while True:
    print("\n1. 도서 목록 조회\n2. 도서 대출\n3. 도서 반납\n4. 도서 추가\n5. 도서 삭제\n6. 도서 수정\n7.도서 설명 \n8. 글씨 크기 조절 \n9. 종료")
    choice = input("번호를 선택하세요: ")

    if choice == "1":
        library.show()
    elif choice == "2":
        index = int(input("대출할 도서 번호: "))
        library.borrow(index)
    elif choice == "3":
        index = int(input("반납할 도서 번호: "))
        library.return_(index)
    elif choice == "4":
        title = input("도서 제목: ")
        author = input("저자: ")
        description = input("도서 설명: ")
        library.add(title, author, description)
    elif choice == "5":
        index = int(input("삭제할 도서 번호: "))
        library.remove(index)
    elif choice == "6":
        index = int(input("수정할 도서 번호: "))
        title = input("새 제목: ")
        author = input("새 저자: ")
        description = input("새 설명: ")
        library.edit(index, title, author, description)
    elif choice == "7":
        index = int(input("설명을 볼 도서 번호: "))
        library.show_description(index)
    elif choice == "8":
        scale = int(input("글씨 크기 (1: 기본, 2: 크게, 3: 더 크게): "))
        library.set_font_scale(scale)
    elif choice == "9":
      print("이용해 주셔서 감사합니다!")
      break
    else:
        print("올바른 번호를 입력하세요.")
