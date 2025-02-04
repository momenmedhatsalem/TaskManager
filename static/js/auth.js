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
    // If no refresh token, redirect to login
    if (!refreshToken) {
    window.location.href = "/login/";
    }
    else {
      let refreshResponse = await fetch("/api/token/refresh/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ refresh: refreshToken }),
      });

      let refreshData = await refreshResponse.json();
      if (refreshResponse.ok) {
        localStorage.setItem("access_token", refreshData.access);
        return fetchWithAuth(url, method, body); // Retry request
      } else {
        console.log("Session expired. Redirecting to login...");
        localStorage.clear();
        window.location.href = "{% url 'login' %}"; // Redirect to login page
      }
    }
  }

  return response;
}
