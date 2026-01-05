// utils/apiRequest.js

function getCookie(name) {
  const cookieString = document.cookie;
  const cookies = cookieString.split('; ');
  for (let cookie of cookies) {
    const [key, value] = cookie.split('=');
    if (key === name) return value;
  }
  return null;
}

export const apiRequest = async (url, options = {}) => {
  const accessToken = getCookie("access_token"); // ← Get token from cookie
  console.log("Cookies:", document.cookie);
  console.log("Access token from cookie:", accessToken);

// Ensure headers object exists
options.headers = {
  ...(options.headers || {}),
  "Content-Type": "application/json",
};

// Only add Authorization header if accessToken exists
if (accessToken) {
  options.headers.Authorization = `Bearer ${accessToken}`;
}
 
try {
  let response = await fetch(url, options);

  if (response.status === 401) {
    console.warn("Access token expired. Attempting refresh...");
      
      // Token expired, attempt to refresh
      const refreshResponse = await fetch("/auth/api/token/refresh/", {
        method: "POST",
        //headers: { "Content-Type": "application/json" },
        credentials: "include",  // Include cookies for refresh
  });


  if (refreshResponse.ok) {
    console.log("Token refreshed. Retrying original request...");
    // Try original request again
    const newAccessToken = getCookie("access_token"); // Refresh likely updated it
    options.headers.Authorization = `Bearer ${newAccessToken}`;
    const retryResponse = await fetch(url, options);
    return retryResponse.ok ? await retryResponse.json() : null;
  } else {
    //commented out for demo
    //alert("Session expired. Please log in again.");
    // window.location.href = "/login"; // Redirect to login if refresh fails
    return null;
  }
}

return response.ok ? response.json() : null;
} catch (error) {
console.error("API request error:", error);
return null;
}
};