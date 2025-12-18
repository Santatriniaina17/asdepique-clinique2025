import { apiUrl } from "../../../app/config";
import type { QueryFormData } from "../types";

export const sendQueryRequest = async (
  credentials: QueryFormData
): Promise<any> => {
  const response = await fetch(`${apiUrl}/autocomplete`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ text: credentials.query }),
  });

  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.message || "Failed");
  }

  return response.json();
};

export const fetchQ = async (credentials: QueryFormData): Promise<any> => {
  const response = await fetch(
    `${apiUrl}/ontology/suggest/${credentials.query}`,
    {
      method: "GET",
    }
  );

  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.message || "Failed");
  }

  return response.json();
};
