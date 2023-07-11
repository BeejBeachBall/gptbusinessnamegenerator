from flask import Flask, request, render_template
import openai

openai.api_key = 'YOUR OPENAI KEY'

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        industry = request.form.get('industry')
        product = request.form.get('product')

        prompt = f"I need to generate a business name for a company in the {industry} industry that sells {product}."

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.5,
            max_tokens=100
        )

        name_ideas = response.choices[0].text.strip().split('\n')

        return render_template('index.html', name_ideas=name_ideas)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
