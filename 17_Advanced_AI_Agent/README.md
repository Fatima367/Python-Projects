**Advanced AI Agent With Chanlit and Chainlit Auth**

*Code for Auth:*
```python
@cl.oauth_callback
def oauth_callback(
    provider_id: str,
    token: str,
    raw_user_data: Dict[str, str],
    default_user: cl.user
) -> Optional[cl.User] :
    """
    Handle the OAuth callback from Github
    Return the user object if authentication is successful, None otherwise
    """

    print(f"Provider: {provider_id}")
    print(f"User data: {raw_user_data}")

    return default_user
```

*Demo data fetching tool from an api:*
```python
@function_tool("get_asharib_data")
def get_asharib_data() -> str:
    """
    Fetches profile data about Asharib Ali from his personal API endpoint.

    This function makes a request to Asharib's profile API and returns information
    about his background, skills, projects, education, work experience, and achievements.

    Returns:
        str: JSON string containing Asharib Ali's profile information
    """

    try:
        response = requests.get("https://www.asharib.xyz/api/profile")
        if response.status_code == 200:
            return response.text
        else:
            return f"Error fetching data: Status code {response.status_code}"
    except Exception as e:
        return f"Error fetching data: {str(e)}"
``` 