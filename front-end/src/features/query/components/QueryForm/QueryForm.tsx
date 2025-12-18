import { Controller, FormProvider, useForm } from "react-hook-form";
import { StyledContainer } from "./queryForm.styles";
import type { QueryFormComponent } from "./queryForm.types";
import Input from "../../../../shared/components/Input/Input";
import type { QueryFormData } from "../../types";
import { useEffect, useState } from "react";
import useQuery from "../../hooks/useQuery";
import { Autocomplete } from "@mui/material";

const QueryForm: QueryFormComponent = () => {
    const [ suggestions, setSuggestions ] = useState<string[]>([])
    const methods = useForm<QueryFormData>()
    const query = methods.watch("query")
    const { sendQuery, fetchQu } = useQuery()

    useEffect(() => {
        const updateSuggestions = async () => {
            if (query?.length) {
                const sugg = await sendQuery(methods.getValues())
                setSuggestions(sugg)
            }
        }
        updateSuggestions()
    }, [query])

    return (
        <StyledContainer>
            <FormProvider {...methods}>
                <Controller
                    name="query"
                    control={methods.control}
                    render={({ field }) => (
                    <Autocomplete
                        freeSolo
                        disableClearable
                        options={suggestions}
                        onInputChange={(_, value) => field.onChange(value)}
                        renderInput={(params) => (
                            <Input
                                {...field}
                                {...params}
                                inputRef={params.InputProps.ref}
                            />
                        )}
                    />
                    )}
                />
            </FormProvider>
        </StyledContainer>
    )
}

export default QueryForm