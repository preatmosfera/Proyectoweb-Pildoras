def importe_total_carro(request):
    total = 0
    """if request.user.is_authenticated:
        carro = request.session.get("carro", {})  # Evita error si no existe la clave
    for key, value in request.session["carro"].items():
        total = total + (float(value["precio"]) * value["cantidad"])"""
    return {"importe_total_carro": total}