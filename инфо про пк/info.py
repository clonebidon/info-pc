import platform
import psutil



def get_cpu_info():
    cpu_info = {
        "Ядра": psutil.cpu_count(logical=False),
        "Потоки": psutil.cpu_count(logical=True),
        "Использование процессора": psutil.cpu_percent(interval=1),
    }
    return cpu_info


def get_memory_info():
    memory_info = {
        "Общая память": f"{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB",
        "Доступная память": f"{round(psutil.virtual_memory().available / (1024 ** 3), 2)} GB",
        "используемая память": f"{round(psutil.virtual_memory().used / (1024 ** 3), 2)} GB",
    }
    return memory_info


def get_disk_info():
    disk_info = {
        "Общее пространство диска": f"{round(psutil.disk_usage('/').total / (1024 ** 3), 2)} GB",
        "Доступное пространство диска": f"{round(psutil.disk_usage('/').free / (1024 ** 3), 2)} GB",
        "Используемое пространство диска": f"{round(psutil.disk_usage('/').used / (1024 ** 3), 2)} GB",
    }
    return disk_info


def get_computer_info():
    system_info = {
        "Система": platform.system(),
        "Узел": platform.node(),
        "Процессор": platform.processor(),
        "Архитектура": platform.architecture(),
        "Версия Python": platform.python_version(),
    }
    cpu_info = get_cpu_info()
    memory_info = get_memory_info()
    disk_info = get_disk_info()

    system_info.update(cpu_info)
    system_info.update(memory_info)
    system_info.update(disk_info)

    return system_info


def main():
    computer_info = get_computer_info()

    print("Информация о компе:")
    for key, value in computer_info.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
