from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)  # 디버그 모드 활성화