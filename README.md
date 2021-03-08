![img](https://lh3.googleusercontent.com/xhmVRBeBUWfEvt5TiZVPhJbyN-9DwLWcYZJVXE6DPdP-z-DW1i8kOXh3i57OEnm54FdvfXKmj8juid2ODu-kkLAGezGkVixrM648h_vG2ovZ4rHGZr9wWSXgIg2kfVoOG7wKTv4RcFKdhmkEUing6P90JpcZ6tb0bFnk6PdzQSEWBqtg8qZwW69ZHp5ESCilMcO-uzGBkagVpJ99802UbIh9PSPChOvmmiENGs38vO8CUC2cEBffoCJ-RfTpyx5zD6hF3ZwqBvcsNRC9-uy-tPmxQj8-4Cv1TD6BctPFSwhoohhD9NOta2bpLET5qEQ3w83jsdzCk8ZYfJuKf_kFtJVSP6aQMjUD8Rs0mIvQkqfK1eH5PxF1qiEmDAL4T27Wcf7Gr3XIImkmb3GU80Lfjir72KVpjvAUuDJ9i2W2MtInS_Fub4r3ERBXUdsvOIMkF4YOHNEptYj4klo9Oxlnk2vqXkZ543AYXfhszpKQELEahne9fipseagRjM1VgM4zwGq-o3aXdYY3BJFp9P6AvKAdq4IpKOHUaovj49Gse234FbVFb9GSLMebBaIRrOWUqdFBJDRbxqWdb1iQNkh3KA-GfuKS0K5eUNnPB6s4egqBVc904K4LCWeGOuLSLcHuCx0stE12hBpH6WvmI9qyX7sLwqFf7Cf_z-KD0mvVcQMnEjRBZnnLsiO-YLg=w1048-h288-no?authuser=0 "Logo")

# Introdution

__Module Havey:__ Tool to create menu, colored (background, foreground) text, menu, etc ...

# Installation (Need root privileges)
###### Note: if you have you are in windows skip step 1 & 2. Download havey source code, You will get your way if you are developer.
[HAVEY ZIP]()
#### 1. Downloading:
    git clone https://github.com/Chergui-Nadjib/havey.git
#### 2.Adding Executable mode to setup.py:
    chmod +x ./havey/setup.py
#### 3. Running Build:
    ./havey/setup.py build
#### 4. Running Install:
    ./havey/setup.py install

# Usage (Top Functions)

> __bcolored:__ Return a colored background text.
>
> ![img](https://lh3.googleusercontent.com/toj_7Jb1TMa_ffE9c6VdMFQg6gWn3rOze3jsTjvpFx3WBmQgndthOmajjeI2KAVt9G9W3tIkYZS7sEWMQxCrXRSkCKP3eDpbxLcr6YA7o103k2xE3vlp0b47Sab0QG8T97xc7L7LZvW07vRI9e9snNnu97WlfwoDgp_2ETx1QnPoYKW5iiflNiFPaAUTjmQ13Uk35avK8oB2v4HlPmhyv0B2TwcgUdUtpUiXzNEKDHQY66w3nTNJPPSZO6x3BtqSys9twM5EpP-npwf5h760kYUgK6nA5NcFxUnU83sTHRIseAC9OmzAqgstPb80z2bO3dfp-p9c28_VZyS7MIPyTni-eTwM19HJV1CjJi7iPcZrkhnDt6tIMY2F_EXa74qPOPVcUO2_8qIY6XNT9qrH17uxYs9NcCNnFXfmJC9lWVPN4iocLUC-9dxccxrphI_o9fM1Ala7YjieiY8H0UdTvZFCn9aaZ5u7zvuiSt6GxAmrtpUhdc01WGYPiQ-JpnaFfFmQc2Eia3r-_ME7ZDVO9qwTnLm9_XVUjbwAZb5qDBCMk_7VkuSY4CGjZLTAZkpzEU2ek1sbG6WT7uCI0qFltNFNsi5kiKb_Wo2LSCqi7RWLLjLQNhLCijDUdDEFogcqw8Czk_xzPoeIGjuFebPPhk41ZY4g6TxcQpFYQVygXypjPRL0Cvmht3xiELg-=w643-h202-no?authuser=0)
> 
> __colored:__ Return a colored foreground text.
> 
> ![img](https://lh3.googleusercontent.com/h450u_0zrJXuMAHb2cD948pVvolYMxoZqBd6u-zJNWF_Bd9SMSQFAElrrRQrwnu-US-OdpitoS1EPG7ltm9H5t6lqIIiPfnzGFztrO4eOn5GUI4sXjlELb5CegBw9oz9C9JyYzpS30rMg_TwDTjoOECfuL3PqH-pO45NBCnwfGQkjxJkHrmd_PhiOE9VGFQhDqRiERPeLaigsppyKn_8mQ4dqKJFc38A-aqu1-ClRx37jNV3ts6kbXkU_3zMYfoFJ2_Zx61wZYQXWhyiiorXsp9uxuRy9dAcQpzoSI0ePU6aJs8JpgOZXH2seR4_HIYaZHOqWDv7jR-eJ5rgM1c4WZHA7yAOybR7wwYFg1arvI9lGX4lEya72LlpTIVNmZDn6EzopdRmPTUh5bxrcVyWSyADvIZkKlmH_P9EhMuswIk-v_xhw-i4iQ8xwIIREmCfl9q4VWoBLFyh6HpXhvVuoh_K1U1MX2mtikalCzaGM40QEqVFAOQspCat9SqGJG7EcrgSF2BrWa9bgiR402AfWWMDZ1nnqDZo1MsD82bz-PNBRIBe7H2L24CLx5gwoIrnUAEkmkELRiALIHd-ShEg3tUklGpnCXKcg0RATI7jD45-_6-hQllH5R_E7qT6d_wJJ1OLcvaXKgtkKE-yOkpTXZZeKfcWiO2QNc0HObK5yDbvQHU-nv0ovUh43Iba=w641-h153-no?authuser=0)
> 
> __progress:__ Animated Dots.
> 
> ![img](https://lh3.googleusercontent.com/0MBKP3drq8F8N-Alzaqi3BzzEvsT_4kUE9SIZjG2EXw9mGKde9-VSWPDg1gNXK2iptMn19JT_1tnXQF7DLsxQuNUUWJxZHOdwDl4-jhdl43t9HDWEd_I_qOvgugJyBOHahM75xb5D5pGvcSZz7eYpSfUgHO1TiEVKqHD76Yy5g8FYdgzYmSWWVe5X78SNRPxvgW5rSS4mCFPWhJydsF8I6Q4N1Dtvu2IQPBWPX6XMlpGXdQ6L1XB2H5UqBerD_Spff_6IY8bgWV-crTXQ2BZdMsOxc_9LyaPfYJWNiSYcr9TKjtT7ELgn6uXUQJZlR9XCXMtGhflP68xmkjfHN1vZuwM6WbKRO9L5v_1FgvFvj9VKYaBXl3_Q6PGSLNTu4H6oP0CFi00uvcOKf6SYhVr-RX4t5X0TpuPmOFk8uiGxYl_q4LeW4QFZWleIIQR-rlJ6i3eSHF6RPYcAaE-A3OItbHRcP4PxxYO8Jd6vCVIyG2YI0Hw7jnvlGfYECORj8_G1jC9prLkG7-M7hWMoeWDYbMRZfmyeXg7LJqnG1WcKtnex45esjMciG4JjFjbryZypQNRoTWWD1SR4AUfmKO0SahUZlere_i9dweajNV06K39Vu_YzfCUo1h38GYXX7COeJ-YCUdma7hD_Fqtm-9DjE8FayEDrvSRYBsCYRab8orXgsToa2g5z8N-CU5N=w644-h172-no?authuser=0)

# Requirements
> - Python
>
> - Colorama
>
> - Setuptools
> 
> - Git

# License

[Read on GNU.ORG](https://www.gnu.org/licenses/gpl-3.0.txt)
