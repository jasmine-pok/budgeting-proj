function getTokenFromCookies() {
  console.log(document.cookie);
  const match = document.cookie.match(/(^| )access_token=([^;]+)/);
  return match ? match[2] : null;
  
}

// utils/apiRequest.js
export const apiRequest = async (url, options = {}) => {
  const accessToken = getTokenFromCookies();  // Get token from cookies
  console.log(accessToken);
  if (!accessToken) {
    console.warn("No access token available. Authentication required.");
    return null;  // Prevent unauthorized requests
  }

   // Include the Authorization header
   options.headers = {
    ...options.headers,
    Authorization: `Bearer ${accessToken}`,  // Add token to Authorization header
  };

  // Ensure options has correct settings
  options.credentials = "include"; // Automatically include cookies

try {
  const response = await fetch(url, options);

  if (response.status === 401) {
      // Token expired, attempt to refresh
      const refreshResponse = await fetch("http://3.144.107.209/api/token/refresh", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",  // Include cookies for refresh
  });


  if (refreshResponse.ok) {
    const data = await refreshResponse.json();
    // Assuming the refresh returns the new access token, set it in the cookies
    document.cookie = `access_token=${data.access}; path=/`; // Set new access token in cookies

    // Retry the original request with the new token
    options.headers.Authorization = `Bearer ${data.access}`;
    return await fetch(url, options).then(res => res.json());
  } else {
    alert("Session expired. Please log in again.");
    window.location.href = "/login"; // Redirect to login if refresh fails
    return null;
  }
}

return response.ok ? response.json() : null;
} catch (error) {
console.error("API request error:", error);
return null;
}
};