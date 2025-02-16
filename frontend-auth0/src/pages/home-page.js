import React from "react";
import { Auth0Features } from "../components/auth0-features";
import { HeroBanner } from "../components/hero-banner";
import { PageLayout } from "../components/page-layout";
import{StateButton} from "../components/buttons/enable-disable-button";
import { useAuth0 } from "@auth0/auth0-react";
import { useEffect,useState } from "react";

//const API_URL = "http://localhost:8000/api/private";
const API_URL = "http://localhost:8000/users/onboard";

export const HomePage = () => {

  const [gmailPermissionStatus, setGmailPermissionStatus] = useState(false);
  const { getAccessTokenSilently, isAuthenticated, loginWithRedirect } = useAuth0();

  // Function to handle button action
  const handlePermissionChange = async (newStatus) => {
    console.log("Permission status changed:", newStatus);
    const token = await getAccessTokenSilently();

    const response = await fetch(API_URL, {
      method: "GET",
      headers: {
        Authorization: `Bearer ${token}`, // Send token to FastAPI
      },
    });

    console.log("API response:", response);
    // Call gmail oauth api and redirect here.
    console.log("permission is called");
    setGmailPermissionStatus(newStatus);
    // Perform any action here (e.g., request permission from API, update DB)
  };

return(
  <PageLayout>
    <HeroBanner />
    <Auth0Features />
    <h2>Permission Control</h2>
    <button onClick={handlePermissionChange} class="button button-primary" >Gmail Auth 1</button>
      <StateButton
        buttonName="Gmail Authorization"
        initialStatus={gmailPermissionStatus}
        onAction={handlePermissionChange}
      />
      <p>Current Status: {gmailPermissionStatus ? "Enabled" : "Disabled"}</p>

  </PageLayout>);
};
