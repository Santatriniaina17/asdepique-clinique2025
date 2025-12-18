import { FormProvider, useForm } from "react-hook-form";
import { StyledContainer } from "./queryForm.styles";
import type { QueryFormComponent } from "./queryForm.types";
import Input from "../../../../shared/components/Input/Input";
import type { QueryFormData } from "../../types";
import { useEffect } from "react";
import useQuery from "../../hooks/useQuery";

const QueryForm: QueryFormComponent = () => {
    const methods = useForm<QueryFormData>()
    const query = methods.watch("query")
    const { sendQuery, fetchQu } = useQuery()

    useEffect(() => {
        sendQuery(methods.getValues())
    }, [query])

    return (
        <StyledContainer>
            <FormProvider {...methods}>
                <Input
                    variant="filled"
                    label="Soraty eto pr"
                    name="query"
                    type="text"
                />
            </FormProvider>
        </StyledContainer>
    )
}

export default QueryForm