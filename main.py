import test_sync
import test_async
from time import time

init = time()
print(15 * "+=", "Iniciando Test Sync", 15 * "=+")
test_sync.main()
tempo_sync = time()-init
print(10 * "+=", f"Test Sync Finalizado em {tempo_sync:.2f} Seg", 10 * "=+")



init = time()
print(15 * "+=", "Iniciando Test Async", 15 * "=+")
test_async.main()
tempo_async = time()-init
print(12 * "+=", f"Test Async Finalizado em {tempo_async:.2f} Seg", 12 * "=+")


porcentagem = 1 - (tempo_async/tempo_sync)
print(f"Async foi {porcentagem:.2f}% mais eficiente que Sync")