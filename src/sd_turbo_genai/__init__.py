import torch #Ejecutar operaciones MAtmaticas de modelo
from diffusers import AutoPipelineForText2Image
#Diffusers es una libreria especialazada en modelos generativos

print("Cargar el modelo...")

modelo = AutoPipelineForText2Image.from_pretrained(
    "stabilityai/sd-turbo",
    torch_dtype=torch.float32#float16 o float32
    #torch.floatXX, imdica la precision numerica con que carga los pesos
    # (decimales, la precision para generar la imagen el maas preciso es 32)
)

modelo = modelo.to("cpu")

prompt = input("Escribe el prompt de la iamgen que quieres crear: ")
negative_prompt = "(peor calidad, baja resolución:1.4), (imagen borrosa, desenfoque:1.2), artefactos de compresión, anatomía defectuosa, extremidades deformadas, mutaciones, feo, texto, marcas de agua, firmas, logotipos, colores lavados"
print("imagen en curso....")


imagen = modelo(
    prompt=prompt,#Intrucciones o detalles para crear la iamgen
    negative_prompt= negative_prompt,
    num_inference_steps=10,# las veces que va tratar de crear o refinar la imagen
    guidance_scale=2.0# Que tan fiel debe ser el prompt (creatividad)
).images[0]

imagen.save("imagen.png")
print("imagen Guardada")

