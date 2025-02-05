async function fetchWithAuth(url, method = "GET", body = null) {
  let token = localStorage.getItem("access_token");

  let headers = {
    "Content-Type": "application/json",
    Authorization: "Bearer " + token,
  };

  let response = await fetch(url, {
    method: method,
    headers: headers,
    body: body ? JSON.stringify(body) : null,
  });

  if (response.status === 401) {
    // Unauthorized - token may be expired
    const refreshToken = localStorage.getItem("refresh_token");

    if (!refreshToken) {
      localStorage.clear(); // Ensure we clear all stored tokens
      window.location.href = "/login/";
      return;
    }

    try {
      let refreshResponse = await fetch("/api/token/refresh/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ refresh: refreshToken }),
      });

      if (!refreshResponse.ok) {
        throw new Error("Refresh token invalid");
      }

      let refreshData = await refreshResponse.json();
      if (refreshData.access) {
        localStorage.setItem("access_token", refreshData.access);
        return fetchWithAuth(url, method, body); // Retry request
      }
    } catch (error) {
      console.error("Session expired. Redirecting to login...", error);
      localStorage.clear();
      window.location.href = "/login/";
    }
  } else if (!response.ok) {
    throw new Error(`Request failed with status ${response.status}`);
  }

  return response;
}

// isAuthenticated function that checks through backend if the user is authenticated
async function isAuthenticated() {
  let response = await fetchWithAuth("/api/tasks/");
  return response.ok;
}
