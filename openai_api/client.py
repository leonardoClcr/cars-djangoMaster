from openai import OpenAI


client = OpenAI(
    api_key='sk-proj-dhCACjg6ufJkWmlJhQDiT3BlbkFJOoHr6HVBAu2w9NB8Zb69'
)


def get_car_ai_bio(model, brand, year):
    message = '''
    Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisa especificas desse modelo de carro.
    '''
    message = message.format(brand, model, year)
    response = client.chat.completions.create(
        messages =[
            {
                'role':'user',
                'content':'message'
            }
    ],
    max_tokens=1000,
    model='gpt-3.5-turbo',
    )

    return response.choices[0].message.content