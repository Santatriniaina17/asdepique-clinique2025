import { useMutation } from "@tanstack/react-query";
import type { QueryFormData } from "../types";
import { fetchQ, sendQueryRequest } from "../api/query.api";

const useQuery = () => {
  const {
    mutateAsync: sendQuery,
    isPending: isLoading,
    error,
  } = useMutation({
    mutationFn: async (credentials: QueryFormData) => {
      const { suggestions } = await sendQueryRequest(credentials);
      const { matches } = await fetchQ(credentials);

      return { suggestions, domain: matches?.[0]?.suggestions?.[0] };
    },
  });

  const fetchQu = async () => {
    try {
    } catch (error) {
      console.error("Error fetching:", error);
      throw error;
    }
  };

  return { sendQuery, isLoading, error, fetchQu };
};

export default useQuery;
