# @require_http_methods(["POST"])

#
# def add_product(request):
# # Parsear el cuerpo de la solicitud
# try:
#     product_data = json.loads(request.body)
# except json.JSONDecodeError:
#     return JsonResponse({'error': 'Invalid JSON format'}, status=400)
#
#     #                    Insertar el producto en la colección
# result = productos_collection.insert_one(product_data)
#
# # Convertir _id a string para evitar problemas de serialización
#
#
# product_data['_id'] = str(result.inserted_id)
#
# # Imprimir los datos del producto (para depuración)
# print(product_data)
#
# # Devolver el product_data con el _id convertido a string
# return JsonResponse({'data': product_data})

# Carlos 1 - Lucas  0

# @require_http_methods(["GET"])
# def get_products(request):
#     try:
#         # Obtener todos los documentos de la colección
#         documents = list(productos_collection.find({}))
#
#         # Serializar los documentos
#         serialized_documents = [serialize_document(doc) for doc in documents]
#
#         # Devolver los documentos serializados en formato JSON
#         return JsonResponse(serialized_documents, safe=False)
#
#     except Exception as error:
#         # Manejar errores y devolver un mensaje adecuado
#         return JsonResponse({'error': 'Failed to retrieve products', 'message': str(error)}, status=500)
