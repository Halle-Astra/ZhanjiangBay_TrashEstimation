function value = get_value(site,site1)
[x,~] = sort(abs(site-site1));
value = x(0);