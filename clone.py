from pywebcopy import save_website

url = ''#aqi va la url de la pagina que quieras descargar
project_folder = 'C:\\Users\\crhac\\OneDrive\\Escritorio\\datos'
project_name = ''#aqui va el nombre del archivo que quieras como se llame
kwargs = {
    'project_name': project_name,
    'bypass_robots': True,
    'debug': True,
}
save_website(url=url, project_folder=project_folder, **kwargs)
