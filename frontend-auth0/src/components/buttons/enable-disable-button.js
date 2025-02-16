import React, { useState, useEffect } from "react";

export const StateButton = ({ buttonName, initialStatus, onAction }) => {
  const [isEnabled, setIsEnabled] = useState(initialStatus);

  useEffect(() => {
    setIsEnabled(initialStatus); // Update state if prop changes
  }, [initialStatus]);

  const handleClick = () => {
    const nextStatus = !isEnabled; // Toggle state
    setIsEnabled(nextStatus);
    
    if (onAction) {
      onAction(nextStatus); // Call the provided function with next status
    }
  };
  return (
    <button onClick={handleClick} class="button button-primary" disabled="false">
      {buttonName} {isEnabled ? "(Enabled)" : "(Disabled)"}
    </button>
  );
};
