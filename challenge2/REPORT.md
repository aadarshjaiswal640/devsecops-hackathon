Command Injection
The application used os.system() with unsanitized user input. An attacker could inject additional shell commands and execute arbitrary commands on the server. This may lead to data theft, system compromise, or denial of service. Using subprocess.run() with validated input prevents shell command execution.

SQL Injection
The application constructed SQL queries using string interpolation. An attacker could modify the query logic and access unauthorized records from the database. Parameterized queries separate data from SQL commands and prevent malicious input from being executed.

Insecure Deserialization
The application used pickle.loads() on untrusted input. A crafted pickle payload can execute arbitrary Python code during deserialization. This could result in complete server compromise. Replacing pickle with JSON removes code execution risks because JSON only represents data.