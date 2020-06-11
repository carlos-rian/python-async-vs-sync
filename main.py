
from project import test_sync
from project import test_async
from time import time

init = time()
print(15 * "+=", "Iniciando Test Sync", 15 * "=+")
test_sync.main()
print(10 * "+=", f"Test Sync Finalizado em {time()-init:.2f} Seg", 10 * "=+")



init = time()
print(15 * "+=", "Iniciando Test Async", 15 * "=+")
test_async.main()
print(10 * "+=", f"Test Async Finalizado em {time()-init:.2f} Seg", 10 * "=+")

