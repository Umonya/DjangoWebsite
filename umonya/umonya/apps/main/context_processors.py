def dynamic_menu(request):
    # Adds Dynamic Menu Template Context
    from models import Dynamic_Section
    try:
        return{"registration": Dynamic_Section.objects.get(section="registration")}
    except:
        return {"registration": False}
