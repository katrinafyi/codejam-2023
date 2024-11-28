{-# LANGUAGE DuplicateRecordFields, FlexibleInstances, UndecidableInstances #-}

module Main where

import Control.Monad
import Data.Array
import Data.Char
import Data.Bits
import Data.List
import Data.List.Split
import Debug.Trace
import System.Environment
import System.IO
import System.IO.Unsafe

--
-- Complete the 'unjumble' function below.
--
-- The function is expected to return a STRING.
-- The function accepts STRING jumbled_text as parameter.
--

unjumble [] = []
unjumble jumbled_text
    | null front = x1 ++ unjumble x2
    | length front > 2 = (h : reverse mid) ++ (t : unjumble rest)
    | otherwise = front ++ unjumble rest
    where 
        (x1,x2) = span (not . isLetter) jumbled_text
    
        (front,rest) = span isLetter jumbled_text
        (h:xx) = front -- span of isLetter
        mid = init xx
        t = last xx
        


main :: IO()
main = do
    stdout <- getEnv "OUTPUT_PATH"
    fptr <- openFile stdout WriteMode

    jumbled_text <- getLine

    let unjumbled_text = unjumble jumbled_text

    hPutStrLn fptr unjumbled_text

    hFlush fptr
    hClose fptr
