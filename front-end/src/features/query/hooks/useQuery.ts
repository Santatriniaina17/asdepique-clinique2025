import { useMutation } from "@tanstack/react-query"
import type { QueryFormData } from "../types"
import { fetchQ, sendQueryRequest } from "../api/query.api"

const useQuery = () => {
    const { mutateAsync: sendQuery, isPending: isLoading, error } = useMutation({
        mutationFn: async (credentials: QueryFormData) => {
            const response = await sendQueryRequest(credentials)
        },
    })

    const fetchQu = async () => {
        try {
            const data = await fetchQ()
            return data
        } catch (error) {
            console.error("Error fetching:", error)
            throw error
        }
    }

    return { sendQuery, isLoading, error, fetchQu }
}

export default useQuery