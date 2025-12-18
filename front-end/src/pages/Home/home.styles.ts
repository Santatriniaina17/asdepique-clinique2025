import { styled } from "@mui/material/styles";
import { Stack } from "@mui/material";

export const StyledContainer = styled(Stack)(({ theme }) => ({
    background: theme.custom.background,
    height: "100vh",
    alignItems: "center",
    justifyContent: "center",
}))