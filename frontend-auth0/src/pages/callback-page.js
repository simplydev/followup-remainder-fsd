import { useAuth0 } from "@auth0/auth0-react";
import React from "react";
import { NavBar } from "../components/navigation/desktop/nav-bar";
import { MobileNavBar } from "../components/navigation/mobile/mobile-nav-bar";
import { PageLayout } from "../components/page-layout.js";
import { useEffect, useState } from "react";


export const CallbackPage = () => {
  const { error } = useAuth0();

  const { loginWithRedirect, getAccessTokenSilently, isAuthenticated, user } = useAuth0();
  const [gmailToken, setGmailToken] = useState("");

  useEffect(() => {
    if (isAuthenticated) {
      getAccessTokenSilently({
        authorizationParams: {
          audience: "https://www.googleapis.com/",
          scope: "https://www.googleapis.com/auth/gmail.readonly"
        }
      }).then((token) => {
        setGmailToken(token);
      }).catch(console.error);
    }
  }, [isAuthenticated, getAccessTokenSilently]);

  console.log("gmail token", gmailToken);


  if (error) {
    return (
      <PageLayout>
        <div className="content-layout">
          <h1 id="page-title" className="content__title">
            Error
          </h1>
          <div className="content__body">
            <p id="page-description">
              <span>{error.message}</span>
            </p>
          </div>
        </div>
      </PageLayout>
    );
  }

  return (
    <div className="page-layout">
      <NavBar />
      <MobileNavBar />
      <div className="page-layout__content" />
    </div>
  );
};
