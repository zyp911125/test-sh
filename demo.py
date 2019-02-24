import yaml
def main():
    with open("./data.yaml",'r') as f:
        data=yaml.load(f)
        print(type(data))
        print(data)

if __name__ == '__main__':
    main()