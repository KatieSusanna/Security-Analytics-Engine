from concurrent.futures import ThreadPoolExecutor

import attack_bruteforce
import attack_sqli  
import attack_traversal
import attack_ddos


with ThreadPoolExecutor(max_workers=4) as executor:
    executor.submit(attack_bruteforce.run)
    executor.submit(attack_sqli.run)
    executor.submit(attack_traversal.run)
    executor.submit(attack_ddos.run)