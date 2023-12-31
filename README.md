# StudyNow Project Setup Instructions

This README file provides a step-by-step guide to setting up the StudyNow project on your local machine.

## Prerequisites

Make sure you have the following installed on your machine:

- Git
- Python
- pip
- Node.js with npm

If not, please install these before proceeding.

## Setup Instructions

1. **Create the Folder**:

   Begin by creating a new folder named "StudyNow". You can do this manually or via terminal using mkdir command:

   ```
   mkdir StudyNow
   ```

2. **Clone the Repository**:

   Open your terminal and navigate to your new folder location using the `cd` command:

   ```
   cd StudyNow
   ```

   Then, clone the Git repository:

   ```
   git clone https://github.com/waikhin/studynow.git
   ```

3. **Install Python Dependencies**:

   Navigate into the cloned "studynow" folder:

   ```
   cd studynow
   ```

   Install the Python dependencies specified in the requirements.txt file:

   ```
   pip install -r requirements.txt
   ```

4. **Activate the Virtual Environment**:

   Run the project in a virtual environment by activating it:

   ```
   source project_env/Scripts/activate
   ```

   Note: On Windows, you would use the following command instead:

   ```
   .\project_env\Scripts\activate
   ```

5. **Install Vue.js and Project Dependencies**:

   Navigate to the "studynow_vue" folder:

   ```
   cd studynow_vue
   ```

   Install Vue.js using npm:

   ```
   npm install -g @vue/cli
   ```

   Install the necessary project dependencies:

   ```
   npm install
   ```

6. **Run the Development Server**:

   Start the development server:

   ```
   npm run serve
   ```

7. **Access the System**:

   Open your web browser and navigate to the following URL to access the system:

   ```
   http://localhost:8080/
   ```

Enjoy using StudyNow! For any additional information or troubleshooting, please refer to the official documentation or contact the developer team.
