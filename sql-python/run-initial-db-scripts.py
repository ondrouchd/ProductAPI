import subprocess

# the list pf python scripts I want to run
scripts = ['create-database-productdb.py', 'create-table-products.py', 'inser-data-to-products.py', 'read-data-from-products.py']

# for each script in the list run external process
for script in scripts:
    try:
        subprocess.run(['python', script], check=True)
        print(f'{script} ran successfully')
    except subprocess.CalledProcessError as e:
        print(f'Error running {script}')
        print(e)
        break