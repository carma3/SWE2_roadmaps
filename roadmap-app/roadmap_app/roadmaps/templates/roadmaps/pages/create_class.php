<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Class</title>
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>


<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Save Class</button>
</form>