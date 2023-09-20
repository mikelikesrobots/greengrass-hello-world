# Greengrass Hello World

Greengrass component for sending Hello World messages.

## Building the project

1. Create Python virtual environment with all dependencies:

```bash
python3 -m pip install virtualenv
python3 -m virtualenv venv
source ./venv/bin/activate
# OR
./venv/Scripts/activate

pip install git+https://github.com/aws-greengrass/aws-greengrass-gdk-cli.git@v1.3.0
```

2. Build the component:

```bash
cd HelloWorld
gdk component build
```

3. Deploy the component:

On an instance with a Greengrass deployment containing the Greengrass CLI:

```bash
gdk component publish
```

This will automatically create an S3 bucket in the correct account (if needed), deploy component artifacts to it, and register the component in Greengrass ready for deployment.
Note that if a bucket is created, each core device must be granted access to it. See [here](https://docs.aws.amazon.com/greengrass/v2/developerguide/device-service-role.html) for more information.

### Test Locally

To test the component locally, follow the build steps, then use this command instead of deploying:

```bash
cd HelloWorld
sudo /greengrass/v2/bin/greengrass-cli deployment create \
    -a ./greengrass-build/artifacts \
    -r ./greengrass-build/recipes \
    -m "com.mike.HelloWorld=1.0.0"
```

## Project Generation

Project was initially generated from the root using:

```bash
gdk component init --template HelloWorld --language python -n HelloWorld
```
