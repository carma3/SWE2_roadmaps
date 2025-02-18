<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Roadmap</title>
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>

<form method="POST">
    {% csrf_token %}
    {{ form.as_p }} <!-- Automatically renders 'form' fields with labels in <p> elements -->
    <button type="submit">Create</button>
</form>

{% if messages %}
<ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
</ul>
{% endif %}

<p><a href="{% url 'dashboard' %}">Back</a></p>