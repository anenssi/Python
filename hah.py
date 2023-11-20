class Quiz:
    def __init__(self):
        self.questions = [
            {"question": "Скільки планет у Сонячній системі?", "answer": "8"},
            {"question": "Який рік важаеться роком ІІ?", "answer": "2021"},
            {"question": "Що таке Python?", "answer": "Мова програмирования"},
            {"question": "Скільки океанів на планеті Земля?", "answer": "5"},
            {"question": "Яка единиця ізмірювання тока?", "answer": "Ампер"},
        ]

    def get_next_question(self):
        return self.questions.pop(0)

    def run_quiz(self):
        score = 0
        num_questions = 5 

        print("Вітаю на вікторині!")

        for _ in range(num_questions):
            if not self.questions:
                print("Упс! Закінчились питання.")
                break

            current_question = self.get_next_question()
            print("\nВопрос:", current_question["question"])

            user_answer = input("Ваша відповідь: ")

            if user_answer.lower() == current_question["answer"].lower():
                print("Вірно!")
                score += 1
            else:
                print(f"Невірно. Вірна відповідь: {current_question['answer']}")

        print(f"\nПідсумковий рахунок: {score}/{num_questions}. Дякую за уасть!")

if __name__ == "__main__":
    quiz = Quiz()
    quiz.run_quiz()
