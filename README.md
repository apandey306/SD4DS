# Software Design for Data Scientists

This is the code repository that accompanies the book "Software Engineering for Data Scientists" by Catherine Nelson, published by O'Reilly Media.

## Dependencies

I used Python 3.10 while writing the book. You can find package versions in `requirements.txt`

## Setup Instructions

Before you install any packages, create a new virtual environment using the following command on macOS or Linux:

`$ python -m venv SD4DS`

You can replace `SD4DS` with the name of your virtual environment.

Next, activate the virtual environment with this command:

`$ source SEforDS/bin/activate`

For Windows, run
`.\SEforDS\Scripts\activate`

You can change the execution policy by running the following command in your PowerShell as an administrator:
`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

This command sets the policy to RemoteSigned, which means that you can run your own scripts or scripts from trusted publishers without any interruption. You’ll see the name of your virtual environment appear in parentheses before the command prompt, like so:
`(SEforDS)$`

This is common to any of the virtual environment tools above. You can now install packages using pip into your virtual environment. When you’re done with the virtual environment, you can exit it with this command:
`(SEforDS)$ deactivate`

The name of your virtual environment will disappear from the command prompt.

It’s best practice to create a new virtual environment every time you start a new project, activate it, then install the libraries you need for that project. You should keep your system Python installation “clean” and not install any third-party libraries system-wide. This will prevent any conflicts between library versions.

Then run the following to install all required dependencies. 
`pip install -r .\requirements.txt`
