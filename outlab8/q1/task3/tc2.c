int recurse(int n)
{
    if(n == 0) 
	    return 0;
    int ret = recurse(n-1);
    ret = ret + n;
    return ret;
}

int main(int argc, char *argv[])
{
    recurse(10);
    return 0;
}
