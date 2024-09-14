
---

# Installation Guide

This guide will walk you through setting up the necessary environment to run the provided code on Linux, Windows, and Mac. Follow the instructions for your operating system.

---

## **Linux Installation Guide**

Linux tends to provide the smoothest experience for setting up this environment. Follow the steps below:

### 1. Install Fortran Compiler
To start, you need to install the Fortran compiler:

1. Open your terminal.
2. Search for "Fortran compiler" on Google and go to the official Fortran website.
3. You'll find a command for installing Fortran on Linux. For Ubuntu, you can simply use:

    ```bash
    sudo apt-get install gfortran
    ```

This will install the Fortran compiler needed for the project.

### 2. Install Anaconda and Create Environment

Anaconda simplifies Python package management and environment setup. To install it:

1. Download the Anaconda installer for Linux from [here](https://www.anaconda.com/products/distribution).
2. Once downloaded, open the terminal and run the following command to start the installation:

    ```bash
    bash ~/Downloads/Anaconda3-<version>-Linux-x86_64.sh
    ```

    Follow the prompts to complete the installation.

3. After Anaconda is installed, create a new environment with Python 3.8:

    ```bash
    conda create -n your_env_name python=3.8
    ```

4. Activate the environment:

    ```bash
    conda activate your_env_name
    ```

### 3. Install PyTorch

Now, install PyTorch inside the Anaconda environment:

1. Visit the [PyTorch website](https://pytorch.org/get-started/locally/), select your system specifications, and copy the appropriate installation command for Linux.
2. For example, for a CPU-only installation:

    ```bash
    conda install pytorch torchvision torchaudio cpuonly -c pytorch
    ```

3. If you have a GPU and would like to use CUDA, install the CUDA version of PyTorch:

    ```bash
    conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
    ```

### 4. Install Additional Packages

In the provided code, there is an installation section where you need to install some additional packages:

1. Uncomment the last three lines in that section and run them. For example:

    ```bash
    # Uncomment these lines:
    # !pip install package_name
    # !pip install another_package
    ```

### 5. Done!
Once all the above steps are complete, you’re all set up and ready to go!

---

## **Windows Installation Guide**

Setting up on Windows requires a few extra steps, but it's still straightforward.

### 1. Install Fortran Compiler

To install the Fortran compiler on Windows:

1. Download and install `MinGW` from the [MinGW website](https://osdn.net/projects/mingw/releases/).
2. During installation, make sure to select the Fortran Compiler option.
3. After installation, add the `MinGW` path to your system’s environment variables:
   - Open **Control Panel** > **System** > **Advanced System Settings** > **Environment Variables**.
   - In the **System variables** section, find `Path`, click **Edit**, and add the path to your MinGW installation (e.g., `C:\MinGW\bin`).

### 2. Install Anaconda and Create Environment

1. Download the Windows version of [Anaconda](https://www.anaconda.com/products/distribution).
2. Run the installer and follow the prompts to install Anaconda.
3. Once installed, open **Anaconda Prompt** and create a new environment with Python 3.8:

    ```bash
    conda create -n your_env_name python=3.8
    ```

4. Activate the environment by running:

    ```bash
    conda activate your_env_name
    ```

### 3. Install PyTorch

Now, install PyTorch within the environment:

1. Go to the [PyTorch installation page](https://pytorch.org/get-started/locally/), choose your Windows specifications, and copy the relevant installation command.
2. For a CPU-only installation:

    ```bash
    conda install pytorch torchvision torchaudio cpuonly -c pytorch
    ```

3. If you have a GPU and want to use CUDA, ensure that your GPU drivers are installed, and then install the CUDA version of PyTorch:

    ```bash
    conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
    ```

### 4. Install Additional Packages

1. In the code provided, there's a section with package installations. Uncomment the necessary lines and run them:

    ```bash
    # Uncomment these lines in your script:
    # !pip install package_name
    # !pip install another_package
    ```

### 5. Done!
Once you have completed these steps, you're ready to start running your code.

---

## **Mac Installation Guide**

Setting up on Mac is similar to Linux with a few minor differences.

### 1. Install Fortran Compiler

To install the Fortran compiler on Mac:

1. Open **Terminal**.
2. If you don’t have [Homebrew](https://brew.sh/) installed, install it by running:

    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

3. Once Homebrew is installed, run the following command to install the Fortran compiler:

    ```bash
    brew install gcc
    ```

4. `gfortran` comes bundled with the GCC package.

### 2. Install Anaconda and Create Environment

1. Download the Mac version of [Anaconda](https://www.anaconda.com/products/distribution).
2. Run the installer by double-clicking the downloaded file and follow the on-screen instructions.
3. After installation, open **Terminal** and create a new environment with Python 3.8:

    ```bash
    conda create -n your_env_name python=3.8
    ```

4. Activate the environment:

    ```bash
    conda activate your_env_name
    ```

### 3. Install PyTorch

1. Visit the [PyTorch installation page](https://pytorch.org/get-started/locally/), select Mac as your operating system, and copy the appropriate command.
2. For a CPU-only installation, run:

    ```bash
    conda install pytorch torchvision torchaudio cpuonly -c pytorch
    ```

3. For a CUDA-supported version (if using an external GPU):

    ```bash
    conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
    ```

### 4. Install Additional Packages

1. In the provided code, you’ll find a section where extra packages need to be installed. Uncomment the last three lines and run them:

    ```bash
    # Uncomment these lines in your script:
    # !pip install package_name
    # !pip install another_package
    ```

### 5. Done!
Once the above steps are completed, your environment is ready to go!

---

With these step-by-step guides, you should be able to set up the environment on Linux, Windows, and Mac without any issues. If you encounter any problems along the way, feel free to search for solutions online or reach out for help!
