import { styled } from "@mui/material/styles";
import { Stack } from "@mui/material";
const imgHeight = 120;

export const StyledContainer = styled(Stack)(({ theme }) => ({
    background: theme.custom.header,
    position: "relative",
    height: `${imgHeight * 0.6}px`,
    marginBottom: `${imgHeight * 0.4}px`,
    "& .img_ispm": {
        width: `${imgHeight}px`,
        background: theme.custom.background,
        borderRadius: "50%",
        padding: "15px",
        boxSizing: "border-box",
        position: "absolute",
        left: "50%",
        transform: "translateX(-50%)",
    },
}))