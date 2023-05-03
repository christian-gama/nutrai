import os
import openai

from diet.models import Diet

from .models import Plan

openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_diet_plan(diet: Diet):
    prompt = get_prompt(diet)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.15,
    )

    planResponse = response.choices[0].text.strip()
    plan = Plan.objects.create(
        diet=diet,
        diet_plan=planResponse
    )
    plan.save()

    return planResponse


def get_prompt(diet: Diet):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    with open(os.path.join(BASE_DIR, 'prompt.txt'), 'r') as f:
        content = f.read()
        output = content.replace('{{duration_in_weeks}}', str(diet.duration_in_weeks)) \
            .replace('{{goals}}', diet.goals) \
            .replace('{{allowed_foods}}', diet.allowed_foods) \
            .replace('{{restricted_foods}}', diet.restricted_foods) \
            .replace('{{meal_plan}}', diet.meal_plan) \
            .replace('{{nutritional_info}}', diet.nutritional_info) \
            .replace('{{cost_in_usd}}', str(diet.cost_in_usd))

        return output
