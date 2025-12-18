import { apiUrl } from '../../../app/config'
import type { QueryFormData } from '../types'

export const sendQueryRequest = async (credentials: QueryFormData): Promise<any> => {

  const response = await fetch(`${apiUrl}/query/send`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(credentials),
  })

  if (!response.ok) {
    const error = await response.json()
    throw new Error(error.message || 'Failed')
  }

  return response.json()
}

export const fetchQ = async(): Promise<any> => {
  const response = await fetch(`${apiUrl}/query/fetch`, {
    method: 'GET'
  })

  if (!response.ok) {
    const error = await response.json()
    throw new Error(error.message || 'Failed')
  }

  return response.json()
}