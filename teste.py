import asyncio
import asyncpg
import platform

async def test():
    try:
        print("Tentando conectar...")
        conn = await asyncpg.connect("postgresql://postgres:Enigma.1@127.0.0.1:5433/workout")
        print("Conectado com sucesso!")
        await conn.close()
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")

# 👇 Corrige o loop no Windows
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

asyncio.run(test())